const fs = require("fs");
const path = require("path");
const _ = require("lodash");

const gabaritoFile = fs.readFileSync("dados/gabarito.json", "utf8");
const gabarito = JSON.parse(gabaritoFile);
const certas = (d, g) => [
  d.rebanho1 === g.rebanho1 ? "O" : "X",
  d.rebanho2 === g.rebanho2 ? "O" : "X",
  d.rebanho3 === g.rebanho3 ? "O" : "X",
  d.rebanho4 === g.rebanho4 ? "O" : "X",
  d.rebanho5 === g.rebanho5 ? "O" : "X",
  d.peixe1 === g.peixe1 ? "O" : "X",
  d.peixe2 === g.peixe2 ? "O" : "X",
  d.peixe3 === g.peixe3 ? "O" : "X",
  d.peixe4 === g.peixe4 ? "O" : "X",
];

const files = [];

for (let i = 0; i < 2; i++) {
  for (let u = 0; u < 6; u++) {
    const codigo = `${i === 0 ? "a" : "b"}${u + 1}`;
    const filePath = path.resolve("dados", codigo, `tcc_result_${codigo}.json`);

    if (!fs.existsSync(filePath)) continue;
    const file = fs.readFileSync(filePath, "utf8");
    if (file === null) continue;
    files.push(file);
  }
}

const result = [];

files.forEach((file) => {
  const dados = JSON.parse(file);
  result.push({
    [dados.codigo]: certas(dados, gabarito),
  });
});

result.forEach((r) => {
  console.log(_.keys(r)[0], ",", _.values(r)[0].join(" , "));
});
