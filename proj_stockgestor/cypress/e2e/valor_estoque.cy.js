describe('Valor_do_estoque', () => {

  it('O usuário incluiu um produto na lista de produtos cadastrados.', () => {

      cy.visit('http://127.0.0.1:8000/');
      cy.wait(60);
      cy.get('.login-button').click();
      cy.wait(60); 
      cy.get('#username').type('cesarschool');
      cy.get('#password').type('Dj@ngo2024');
      cy.wait(60);
      cy.get('.btn').click();
      cy.wait(500);
      cy.get('[href="/valor_estoque/"] > .btn').click();
      cy.wait(2000);
      cy.get('[href="/cadastro_produto/"] > .btn').click();
      cy.wait(60);
      cy.get(':nth-child(2) > .form-control').type('Apple watch SE');
      cy.wait(60);
      cy.get(':nth-child(3) > .form-control').type('watchse');
      cy.wait(60);
      cy.get(':nth-child(4) > .form-control').type('Apple');
      cy.wait(60);
      cy.get(':nth-child(5) > .form-control').type('acessórios');
      cy.wait(60);
      cy.get('.col-8 > .form-control').type('A3');
      cy.wait(60);
      cy.get(':nth-child(7) > .form-control').type('Apple');
      cy.wait(60);
      cy.get('.col-md-8 > .form-control').type('2024-05-02');
      cy.get(':nth-child(9) > .form-control').type('2030-05-02');
      cy.wait(60);
      cy.get(':nth-child(10) > .form-control').type('321');
      cy.wait(60);
      cy.get(':nth-child(11) > .form-control').type('1');
      cy.wait(60);
      cy.get(':nth-child(12) > .form-control').type('578849044');
      cy.wait(60);
      cy.get(':nth-child(13)').type('500');
      cy.wait(60);
      cy.get(':nth-child(14) > .form-control').type('Apple watch preto');
      cy.wait(60);
      cy.get('.d-flex > a > .btn').click();
      cy.wait(60);
      cy.get('[href="/valor_estoque/"] > .btn').click();
      cy.wait(60);  
      cy.get(':nth-child(3) > .table > tbody > tr > :nth-child(1)').invoke('text').should('contain', "ESTOQUE");
      cy.wait(2000);
  })
})
