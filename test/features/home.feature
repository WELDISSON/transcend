# language: pt
Funcionalidade: Validação da home do transcend

  @1
  Cenário: validação da logo
  Dado que eu esteja na home
  Então valido a logo do transcend

  Cenário: validacão dos links do menu
  Dado que eu esteja na home
  Quando clico no menu
  Então valido os links dos menus
  
  Cenário: validação de redirecionamento
  Dado que eu esteja na home
  Quando clico em About
  Então sou redirecionado para página de About

  Cenário: validação de redirecionamento
  Dado que eu esteja na home
  Quando clico em Services
  Então sou redirecionado para página de Services

  Cenário: validação de redirecionamento
  Dado que eu esteja na home
  Quando clico em Contact
  Então sou redirecionado para página de Contact

