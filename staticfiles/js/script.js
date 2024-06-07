import { jsPDF } from 'jspdf';


window.downloadPDF = function() {
    console.log("test")
    var doc = new jsPDF();
    doc.text('Hola mundo!', 10, 10);
    doc.save('hola_mundo.pdf');
}

window.test = function() {
    console.log("test");
};


// window.downloadPDF = downloadPDF;
// window.test = test;