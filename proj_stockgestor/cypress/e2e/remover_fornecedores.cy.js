describe('Como usuário, eu gostaria de remover fornecedores.', () => {

  it('Fornecedores removidos devem desaparecer da lista de fornecedores.', () => {
    
    cy.visit('http://127.0.0.1:8000/');
    cy.get('.login-button').click();
    cy.wait(1000); 

    cy.get('#username').type('cesarschool');
    cy.get('#password').type('Dj@ngo2024');
    cy.get('.btn').click();
    cy.wait(1000);

    cy.get(':nth-child(2) > .nav-link').click();
    cy.wait(1000);

    cy.get(':nth-child(3) > :nth-child(1) > a > img').click();
    cy.wait(1000);

    cy.get(':nth-child(2) > .nav-link').should('not.contain', 'Xiamoi Inc');
  })
})
