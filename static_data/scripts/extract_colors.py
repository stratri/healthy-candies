import pandas as pd
import numpy as np
from PIL import Image
from os import listdir
from matplotlib import colors
import json
from healthy_candies.path import DATA_FOLDER, STATIC_DATA_FOLDER
from os.path import exists, join
from os import listdir

IMAGES_FOLDER = join(DATA_FOLDER, 'images')
TMP_OUTPUT = join(DATA_FOLDER, 'colors.json')

N_HUES = 12
HUES_STR = ['red', 'orange', 'yellow', 'yellow-green', 'green', 'green-cyan',
            'cyan', 'cyan-blue', 'blue', 'blue-magenta', 'magenta', 'pink']

# last one similar to first one is the hue world
REF_HUES = list(np.linspace(0, 1, N_HUES+1))
HUE_BINS = [(a + b) / 2 for a, b in zip([0] + REF_HUES, REF_HUES + [1])]
# Correct the last one to have an including interval for 1
HUE_BINS[-1] = np.nextafter(HUE_BINS[-1], +np.inf)


def extract_arr(arr, i):
    return arr[:, :, i].flatten()


def get_hue_features(img_fp):
    img = Image.open(img_fp)
    # Some images have more than 3 layers, we only want the RGB ones
    arr = np.array(img)[:, :, :3]

    hsv = colors.rgb_to_hsv(arr / 255)  # Values should be between 0 and 1

    H = extract_arr(hsv, 0)
    S = extract_arr(hsv, 1)
    V = extract_arr(hsv, 2)

    # We keep only the values that are not too dark
    mask = (V > 0.5) & (S > 0.6)
    HH = H[mask]
    SS = S[mask]
    VV = V[mask]

    n_vals = HH.shape[0]
    if n_vals == 0:
        return None

    # compute features
    match = np.digitize(HH, HUE_BINS)
    # Merge the last bins in the first one (hue is a cyclic measure 0 = 1)
    match[match == len(HUE_BINS)-1] = 1

    res = {}
    res['total_pix'] = H.shape[0]
    res['total_valid_pix'] = HH.shape[0]

    for i, h_key in zip(range(N_HUES), HUES_STR):
        h_mask = match == i + 1
        res[h_key] = sum(h_mask)  # Take all pixels into account
    return res


def get_colors_from_tmp() -> pd.DataFrame:
    with open(TMP_OUTPUT) as f:
        res = []
        for l in f.readlines():
            res.append(json.loads(l))

    extracted = pd.DataFrame.from_records(res)
    return extracted


if __name__ == '__main__':
    def default(o):
        # For easy encoding
        if isinstance(o, np.int64):
            return int(o)
        raise TypeError

    i = 0
    already_computed = []

    if exists(TMP_OUTPUT):
        df = get_colors_from_tmp()
        already_computed = [code for code in df.code]
    else:
        open(TMP_OUTPUT, 'a').close()

    # extract hue information and save each time in case of crash
    for image_fp in listdir(IMAGES_FOLDER):
        code = image_fp.split('.')[0]

        # Check if don't already have computed this value
        if code in already_computed:
            i += 1
            continue

        fp = join(IMAGES_FOLDER, image_fp)

        try:
            row = get_hue_features(fp)
            if row is None:
                continue
            with open(TMP_OUTPUT, 'a') as f:
                json.dump(dict(code=code, **row), f, default=default)
                f.write('\n')
            i += 1
        except FileNotFoundError:
            pass

    df = get_colors_from_tmp()
    df.to_csv(join(STATIC_DATA_FOLDER, 'colors.csv'), index=False)

    print("Hues from {} images were extracted".format(i))
