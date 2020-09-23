function OnHRButtonClick(){
    document.getElementById("ez").checked = false;
}

function OnEZButtonClick(){
    document.getElementById("hr").checked = false;
}

function OnDTButtonClick(){
    document.getElementById("ht").checked = false;
}

function OnHTButtonClick(){
    document.getElementById("dt").checked = false;
}

function OnCalcButtonClick(){
    var sr = parseFloat(document.getElementById("sr").value);
    var od = parseFloat(document.getElementById("od").value);
    var acc = parseFloat(document.getElementById("acc").value);
    var combo = parseFloat(document.getElementById("combo").value);
    var miss = parseFloat(document.getElementById("miss").value);
    var hd = document.getElementById("hd").checked;
    var hr = document.getElementById("hr").checked;
    var ez = document.getElementById("ez").checked;
    var fl = document.getElementById("fl").checked;
    var dt = document.getElementById("dt").checked;
    var ht = document.getElementById("ht").checked;
    var nf = document.getElementById("nf").checked;

    //strain
    var strain = Math.pow(sr / 10, 3)
    strain *= (1 - (miss / 70))
    strain *= Math.min(Math.pow(2500, 0.11), Math.pow(combo, 0.11))
    strain *= 1.5

    if(hd) strain *= 1.1;
    if(hr) strain *= 1.1;
    if(ez) strain *= 0.9;
    if(fl) strain *= 1.05 + (0.01 * Math.min(Math.pow(2500, 0.1), Math.pow(combo, 0.1)));


    //accuracy
    if(hr) od = Math.min(10, od * 1.4);
    else if(ez) od *= 0.5;
    
    var accuracy = 49.5 - Math.ceil(od * 3);

    if(dt) accuracy /= 1.5;
    if(ht) accuracy /= 0.75;

    
    accuracy = 1 / (Math.pow(accuracy, 5) / 10) + 0.00001;

    accuracy *= Math.pow(acc / 100, 30)
    accuracy *= Math.min(Math.pow(2500, 0.1), Math.pow(combo, 0.1))

    accuracy *= 15000


    pp = Math.pow(strain + accuracy, 1.25) * 300

    if(nf) pp *= 0.9;


    pp_text = document.getElementById("pp");
    pp_text.innerHTML = String(pp.toFixed(2) + "pp");
}