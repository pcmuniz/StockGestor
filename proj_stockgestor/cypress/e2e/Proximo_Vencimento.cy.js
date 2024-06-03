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
      cy.wait(500);

  })
})
