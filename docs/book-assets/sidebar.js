const getPageTocChildren = () => [...document.getElementsByClassName('pagetoc')[0].children];

const pageTocChildren = getPageTocChildren();
const headers = [...document.getElementsByClassName('header')];

// Select highlighted item in ToC when clicking an item
pageTocChildren.forEach((child) => {
    child.addEventHandler('click', () => {
        pageTocChildren.forEach((child) => {
            child.classList.remove('active');
        });
        child.classList.add('active');
    });
});


/**
 * Update highlighted header in ToC when scrolling
 */
const updateFunction = () => {
    let id;
    const pageTocChildren = getPageTocChildren();

    // Calculate which header is the current one at the top of screen
    headers.forEach((header) => {
        if (window.pageYOffset >= header.offsetTop) {
            id = header;
        }
    });

    // Update selected item in ToC when scrolling
    pageTocChildren.forEach((element) => {
        if (id.href.localeCompare(element.href) === 0) {
            element.classList.add('active');
        } else {
            element.classList.remove('active');
        }
    });
};

/**
 * Populate sidebar on load
 */
window.addEventListener('load', () => {
    const pagetoc = document.getElementsByClassName('pagetoc')[0];
    headers.forEach((header) => {
        const link = document.createElement('a');

        // Indent shows hierarchy
        let indent = '0px';
        switch (header.parentElement.tagName) {
            case 'H2':
                indent = '20px';
                break;
            case 'H3':
                indent = '30px';
                break;
            case 'H4':
                indent = '40px';
                break;
            case 'H5':
                indent = '50px';
                break;
            case 'H6':
                indent = '60px';
                break;
            default:
                break;
        }

        link.appendChild(document.createTextNode(header.text));
        link.style.paddingLeft = indent;
        link.href = header.href;
        pagetoc.appendChild(link);
    });
    updateFunction.call();
});

// Handle active headers on scroll
window.addEventListener('scroll', updateFunction);
