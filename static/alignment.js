let start = 1;
let cols = 23;
let rows = 10;
let numsize = 30;
let totalcols = 75;
let totalrows = 6;

function loader(){
  
  let aggregated = document.getElementById("story");

  let panel = document.createElement("h3");
  let title = document.createTextNode("Panel "+start);
  panel.appendChild(title);

  let file = document.createElement("input");
  file.type = "file";
  file.id = "image-"+start;
  file.name = "image-"+start;
  file.accept=".png,.jpg";
  file.required = true;
  let label1 = document.createElement("Label");
  label1.setAttribute("for",file.id);
  label1.innerHTML = "Upload your story image for this panel";

  let brk1 = document.createElement("br");
  brk1.id = "break-one"+start;

  let convo = document.createElement("textarea");
  convo.id = "convo"+start;
  convo.name = "convo"+start;
  //convo.required = true;
  convo.cols = totalcols;
  convo.rows = totalrows;

  let label2 = document.createElement("Label");
  label2.setAttribute("for",convo.id);
  label2.innerHTML = "What will your character say?";


  let brk2 = document.createElement("br");
  brk2.id = "break-two"+start;

  let speech_one = document.createElement("textarea");
  speech_one.id = "speechone"+start;
  speech_one.name = "speechone"+start;
  speech_one.required = true;
  speech_one.placeholder = "First Speech Option";
  speech_one.rows = rows;
  speech_one.cols = cols;

  let speech_two = document.createElement("textarea");
  speech_two.id = "speechtwo"+start;
  speech_two.name = "speechtwo"+start;
//  speech_two.required = true;
  speech_two.placeholder = "Second Speech Option";
  speech_two.rows = rows;
  speech_two.cols = cols;

  let speech_three = document.createElement("textarea");
  speech_three.id = "speechthree"+start;
  speech_three.name = "speechthree"+start;
//  speech_three.required = true;
  speech_three.placeholder = "Third Speech Option";
  speech_three.rows = rows;
  speech_three.cols = cols;

  let brk3 = document.createElement("br");
  brk3.id = "break-three"+start;

  let redir_one = document.createElement("input");
  redir_one.type = "number";
  redir_one.step = "1";
  redir_one.min = "1";
  redir_one.id = "redirone"+start;
  redir_one.name = "redirone"+start;
  redir_one.required = true;
  redir_one.placeholder = "1st option panel redirect";
  redir_one.size = numsize;

  let redir_two = document.createElement("input");
  redir_two.type = "number";
  redir_two.step = "1";
  redir_two.min = "1";
  redir_two.id = "redirtwo"+start;
  redir_two.name = "redirtwo"+start;
//  redir_two.required = true;
  redir_two.placeholder = "2nd option panel redirect";
  redir_two.size = numsize;

  let redir_three = document.createElement("input");
  redir_three.type = "number";
  redir_three.step = "1";
  redir_three.min = "1";
  redir_three.id = "redirthree"+start;
  redir_three.name = "redirthree"+start;
//  redir_three.required = true;
  redir_three.placeholder = "3rd option panel redirect";
  redir_three.size = numsize;

  let brkf = document.createElement("br");
  brkf.id = "break-final"+start;

  let horz = document.createElement("hr");
  horz.id = "horz"+start;

  aggregated.appendChild(panel);

  aggregated.appendChild(label1);
  aggregated.appendChild(document.createElement("br"));
  aggregated.appendChild(file);
  aggregated.appendChild(document.createElement("br"));
  aggregated.appendChild(brk1);
  aggregated.appendChild(label2);
  aggregated.appendChild(document.createElement("br"));
  aggregated.appendChild(convo);
  aggregated.appendChild(brk2);
  aggregated.appendChild(document.createElement("br"));
  aggregated.appendChild(speech_one);
  aggregated.appendChild(speech_two);
  aggregated.appendChild(speech_three);
  aggregated.appendChild(brk3);
  aggregated.appendChild(redir_one);
  aggregated.appendChild(redir_two);
  aggregated.appendChild(redir_three);
  aggregated.appendChild(brkf);
  aggregated.appendChild(horz);
  start = start + 1;
}
