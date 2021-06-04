const oneDay = 24 * 60 * 60 * 1000;
data = new Date();
ano = data.getFullYear();
var dayCount = Math.floor((new Date() - new Date(ano, 0, 01)) / oneDay);

function generateDate() {
    data = new Date();
    monName = new Array("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
    day = data.getDate();
    month = data.getMonth();
    year = data.getFullYear();
    document.getElementById("data").innerHTML = day + " de " + monName[month] + " de " + year;


}


const motivar = () => {
    document.getElementById("data").innerHTML = quotesContainer.quotes[dayCount].quote;
    console.log(quotesContainer.quotes[dayCount].quote);
}