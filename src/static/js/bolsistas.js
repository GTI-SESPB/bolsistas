document.querySelector('input[name=nascimento]').max = new Date().toISOString().split('T')[0];

const mascaraCPF = (e) => {
  let input = e.target;
  let cpf = apenasNumeros(input.value);
  cpf = cpf.replace(/(\d{3})(\d)/,"$1.$2")
  cpf = cpf.replace(/(\d{3})(\d)/,"$1.$2")
  cpf = cpf.replace(/(\d{3})(\d{1,2})$/,"$1-$2")
  input.value = cpf
}

const mascaraCEP = (e) => {
  let input = e.target;
  let cep = apenasNumeros(input.value)
  if (cep.length == 8) getEndereco(cep);
  cep = cep.replace(/(\d{5})(\d)/,'$1-$2');
  input.value = cep;
}

const getEndereco = (cep) => {
  fetch(`https://viacep.com.br/ws/${cep}/json/`)
    .then(response => {
      return response.json();
    })
    .then(json => {
      document.querySelector('input[name=logradouro]').value = json.logradouro;
      document.querySelector('input[name=complemento]').value = json.complemento;
      document.querySelector('input[name=cidade]').value = json.localidade;
    })
}

