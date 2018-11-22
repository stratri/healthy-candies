/**
 * This file is meant to be used to scrap the category tree available at
 * https://tools.wmflabs.org/wikidata-todo/tree.html?q=2095&rp=279
 * 
 * The data can be directly accessed on wikidata, however, this website
 * does a little bit of preprocessing to build the tree, so we decided
 * to use the result directly.
 * 
 * 
 * **How to use ?**
 * Go to the url above. Wait for the page to be fully loaded (label included)
 * Open the browser console (F12), and copy paste the whole file.
 * 
 * The result of the scrap will be directly downloaded.
 */


/**
 * https://stackoverflow.com/a/30800715
 *
 * @param {Object} exportObj
 * @param {String} exportName
 */
function downloadObjectAsJson(exportObj, exportName) {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(exportObj));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", exportName + ".json");
    document.body.appendChild(downloadAnchorNode); // required for firefox
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
}

/**
 * Parses an li element
 *
 * @param {HTMLElement} li
 * @returns {Object}
 */
function parseLi(li) {
    const a = li.children[0];
    const span = a.children[0];
    return { id: span.id, catName: span.innerHTML };
}

/**
 * Parses an ol element
 *
 * @param {HTMLElement} ol
 * @returns {Array}
 */
function parseOl(ol) {
    let res = Array()
    for (const child of ol.children) {
        const tag = child.tagName;
        if (tag === 'OL') {
            res[res.length - 1].childrens = parseOl(child)
        }
        else if (tag == 'LI') {
            res.push(parseLi(child))
        } else {
            throw new Error('Tag not regognized');
        }
    }
    return res;
}


downloadObjectAsJson(
    // we lunch the recursive parsing by passing the root of the tree
    // to the parseOl function
    parseOl(document.getElementById('tree').children[0])[0],
    "categoriesTreeWikiData"
)
