describe('template spec', () => {
  it('passes', () => {
    cy.visit('http://127.0.0.1:8000/');
    cy.get('.login-button').click();
      cy.wait(20); 
      cy.get('#username').type('cesarschool');
      cy.get('#password').type('Dj@ngo2024');
      cy.wait(20);
      cy.get('.btn').click();
      cy.wait(20);
      cy.get('[href="/valor_estoque/"] > .btn').click();
      cy.wait(20);


  })
})  