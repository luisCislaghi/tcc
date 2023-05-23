const fs = require("fs");
const path = require("path");
const _ = require("lodash");
const dayjs = require("dayjs");
dayjs.extend(require("dayjs/plugin/duration"));

const keyString = (e) => _.keys(e)[0];
const key = (e) => parseInt(keyString(e));
const value = (e) => _.values(e)[0];

const formatResult = (d) => {
  const tempo = dayjs.duration(d, "seconds");
  const minutos = tempo.format("m[m]");
  const segundos = tempo.format("s[s]");

  return tempo.minutes() > 0 ? minutos + " " + segundos : segundos;
};

const calculaTempo = (d) => {
  const etapas = d.etapas;
  console.log(d.codigo, etapas, d.final);
  const result = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
  };

  for (let i = 0; i < etapas.length; i++) {
    const atual = etapas[i];
    const proxima = etapas[i + 1];
    const resultKeyAtual = key(atual) + 1;
    const valueAtual = dayjs(value(atual));
    const valueProxima = dayjs(value(proxima));

    // ultima
    if (proxima === undefined) {
      result[resultKeyAtual] = dayjs(d.final).diff(valueAtual, "seconds");
      continue;
    }

    result[resultKeyAtual] =
      result[resultKeyAtual] + valueProxima.diff(valueAtual, "seconds");
  }
  return result;
};

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
    [dados.codigo]: calculaTempo(dados),
  });
});

result.forEach((r) => {
  console.log(
    keyString(r),
    ",",
    _.values(value(r))
      .map((e) => formatResult(e))
      .join(" , ")
  );
});
