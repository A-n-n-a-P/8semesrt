var name_0 = prompt("Роль - Рассказчик");
var name_1 = prompt("Роль - Дедушка");
var name_2 = prompt("Роль - Бабушка");
var name_3 = prompt("Роль - Машенька");
var name_4 = prompt("Роль - Подружка1");
var name_5 = prompt("Роль - Подружка2");

alert (`${name_0}
${name_1}
${name_2}
${name_3}
${name_4}
${name_5}
`)

let div_0 = document.createElement('div');
let div_1 = document.createElement('div');
let div_2 = document.createElement('div');
let div_3 = document.createElement('div');
let div_4 = document.createElement('div');
let div_5 = document.createElement('div');

div_0.className = "msg_0";
div_1.className = "msg_1";

div_0.innerHTML = `Жили-были дедушка да бабушка. Была у них внучка Машенька.
<br>Собрались раз подружки в лес - по грибы да по ягоды. Пришли звать с собой и Машеньку. -  <b> ${name_0} </b>`;
document.body.append(div_0);

div_3.innerHTML = `<br> - Дедушка, бабушка, отпустите меня в лес с подружками! - <b> ${name_3} </b>`;
document.body.append(div_3);

div_0.innerHTML = `hello` + name_0;
document.body.append(div_0);
