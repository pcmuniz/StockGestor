describe('Como usuário, eu gostaria de filtrar produtos por fornecedor', () => {
  it('Na lista de produtos devem aparecer apenas os produtos do fornecedor escolhido pelo usuário.', () => {
    cy.visit('http://127.0.0.1:8000/');
    cy.get('.login-button').click();
    cy.wait(30); 
    cy.get('#username').type('cesarschool');
    cy.get('#password').type('Dj@ngo2024');
    cy.wait(1000);
    cy.get('.btn').click();
    cy.wait(1000); 
    cy.get('.form-select').select('Apple Inc.');
    cy.wait(2000);
    cy.get('.row-cols-lg-auto > :nth-child(3) > .btn').click();

    cy.get('thead > tr > :nth-child(1)').should('not.contain', '34344576', '34343', '34344576');
  });
});


