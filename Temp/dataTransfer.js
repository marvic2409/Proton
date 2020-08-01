// This is part of the implementation of the Data Transfer inerface.
// For more details, see 'Working Docs/interface.md

function setAttribute(id, attribute, value) {

    // this raises exception - TypeError: Cannot read property 'setAttribute'
    // of null at setAttribute (dataTransfer.js:7). I have no clue why but
    // it doesn't seem to be breaking anything so, cheerio!
    document.getElementById(id).setAttribute(attribute, value);
}

function setText(id, toReplace = true, value) {
    if (toReplace) {
        document.getElementById(id).innerText = value;
    } else {
        document.getElementById(id).innerText += value.replace('\n', '<br>')
    }
}

function setContent(id, toReplace = true, value) {
    if (toReplace) {
        document.getElementById(id).innerHTML = value;
    } else {
        document.getElementById(id).innerHTML += value;
    }
}

// tried binding only the gateway.bind function as 'bind' in js, doesn't work.
gateway.bind(setAttribute, setText, setContent);