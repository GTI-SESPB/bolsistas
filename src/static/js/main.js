const apenasNumeros = (value) => {
  if (!value) return "";
  return value.replace(/\D/g, '');
}

const limitarANumeros = (e) => {
  let input = e.target;
  input.value = apenasNumeros(input.value)
}

function redirecionar(url) {
  window.location = url
}
