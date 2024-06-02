describe('Valor_do_estoque', () => {

  it('Como usuário, eu gostaria de remover produtos, após remover deverão desaparecer da lista', () => {

      cy.visit('http://127.0.0.1:8000/');
      cy.wait(60);
      cy.get('.login-button').click();
      cy.wait(60); 
      cy.get('#username').type('cesarschool');
      cy.get('#password').type('Dj@ngo2024');
      cy.wait(60);
      cy.get('.btn').click();
      cy.wait(1000);
      cy.get('[href="/cadastro_produto/"] > .btn').click();
      cy.wait(60);
      cy.get(':nth-child(2) > .form-control').type('AirForce 1');
      cy.wait(60);
      cy.get(':nth-child(3) > .form-control').type('Air1');
      cy.wait(60);
      cy.get(':nth-child(4) > .form-control').type('Nike Inc');
      cy.wait(60);
      cy.get(':nth-child(5) > .form-control').type('Tênis');
      cy.wait(60);
      cy.get(':nth-child(6) > .form-control').type('27463888');
      cy.wait(60);
      cy.get(':nth-child(7) > .form-control').type('2028-05-02');
      cy.wait(60);
      cy.get('.form-select').click();  // Problema aqui
      cy.wait(60);











      cy.get(':nth-child(2) > :nth-child(5) > .btn-danger').click();
      cy.wait(500);

  })
})
