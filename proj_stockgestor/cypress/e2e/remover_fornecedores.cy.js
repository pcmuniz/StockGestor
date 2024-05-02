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
      cy.get(':nth-child(2) > .nav-link').click();
      cy.wait(20);
      cy.get(':nth-child(3) > :nth-child(1) > a > img').click();
      cy.wait(20);
      


      

  })
})  