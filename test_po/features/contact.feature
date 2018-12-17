# language: pt
Funcionalidade: Validação da página Contact

  
  Cenário: validação de redes sociais
  Dado que eu esteja na home
  Quando clico em Contact
  Então valido os links das redes sociais

  Cenário: validação de email válido
  Dado que eu esteja na home
  Quando clico em Contact
  E preencho o email 
  Então valido a mensagem de sucesso

  Cenário: validação de email inválido
  Dado que eu esteja em Contact
  Quando preencho o email inválido
  Então valido a mensagem de erro
