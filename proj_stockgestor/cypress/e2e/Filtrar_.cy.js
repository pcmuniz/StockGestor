describe('Como usuário, eu gostaria de filtrar produtos por fornecedor', () => {

  it('Na lista de produtos devem aparecer apenas os produtos do forncedor escolhido pelo usuário.', () => {
    
    cy.visit('http://127.0.0.1:8000/');
    cy.get('.login-button').click();
      cy.wait(30); 
      cy.get('#username').type('cesarschool');
      cy.get('#password').type('Dj@ngo2024');
      cy.wait(30);
      cy.get('.btn').click();
      cy.wait(30);
      


  })
})