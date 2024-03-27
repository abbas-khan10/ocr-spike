import React, { useEffect } from 'react';

const PdfViewer = () => {
    const fileUrl = "https://clickdimensions.com/links/TestPDFfile.pdf"
    useEffect(() => {
        const pdfObject = require('pdfobject');
        pdfObject.embed(fileUrl + '#toolbar=0', '#pdf-viewer');
    }, [fileUrl]);

    return <div id="pdf-viewer" style={{ height: 600, width: 700}}></div>;
};

export default PdfViewer;