const fs = require("fs");
const path = require("path");
const _ = require("lodash");

const gabaritoFile = fs.readFileSync("dados/gabarito.json", "utf8");
const gabarito = JSON.parse(gabaritoFile);
const certas = (d, g) => [
  d.rebanho1 === g.rebanho1,
  d.rebanho2 === g.rebanho2,
  d.rebanho3 === g.rebanho3,
  d.rebanho4 === g.rebanho4,
  d.rebanho5 === g.rebanho5,
  d.peixe1 === g.peixe1,
  d.peixe2 === g.peixe2,
  d.peixe3 === g.peixe3,
  d.peixe4 === g.peixe4,
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
