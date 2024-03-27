import React, { useEffect } from 'react';
// import PDFObject from "pdfobject"

const PdfViewer = () => {
    const fileUrl = "https://www.orimi.com/pdf-test.pdf"
    useEffect(() => {
        const pdfObject = require('pdfobject');
        pdfObject.embed(fileUrl + '#toolbar=0', '#pdf-viewer');
    }, [fileUrl]);

    return <div id="pdf-viewer" style={{ height: 600, width: 700}}></div>;
};

export default PdfViewer;