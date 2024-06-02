describe('Como usuário, eu gostaria de remover fornecedores.', () => {

  it('Fornecedores removidos devem desaparecer da lista de fornecedores.', () => {
    
    cy.visit('http://127.0.0.1:8000/');
    cy.get('.login-button').click();
    cy.wait(1000); 

    cy.get('#username').type('cesarschool');
    cy.get('#password').type('Dj@ngo2024');
    cy.get('.btn').click();
    cy.wait(2000);

    cy.get(':nth-child(2) > .nav-link').click();
    cy.wait(1000);

    cy.get('[href="/cadastro_fornecedor/"] > .btn').click();
    cy.wait(1000);
    cy.get('.col-11 > .form-control').click().type('Apple Inc');
    cy.wait(100);
    cy.get(':nth-child(3) > .form-control').click().type('12326700');
    cy.wait(100);
    cy.get(':nth-child(4) > .form-control').click().type('1345577');
    cy.wait(100);
    cy.get(':nth-child(5) > .form-control').click().type('145435');
    cy.wait(100);
    cy.get('.col-8 > .form-control').click().type('AV. Cais de Apolo, 77');
    cy.wait(100);
    cy.get(':nth-child(7) > .form-control').click().type('PE');
    cy.wait(100);
    cy.get('.col-md-8 > .form-control').click().type('teste2@gmail.com');
    cy.wait(100);
    cy.get(':nth-child(9) > .form-control').click().type('teste2@gmail.com');
    cy.wait(100);
    cy.get('.col-12 > .btn').click();
    cy.wait(1000);


    cy.get('[href="/cadastro_fornecedor/"] > .btn').click();
    cy.wait(1000);
    cy.get('.col-11 > .form-control').click().type('Samsung Inc');
    cy.wait(100);
    cy.get(':nth-child(3) > .form-control').click().type('12326700');
    cy.wait(100);
    cy.get(':nth-child(4) > .form-control').click().type('13435477');
    cy.wait(100);
    cy.get(':nth-child(5) > .form-control').click().type('1453543');
    cy.wait(100);
    cy.get('.col-8 > .form-control').click().type('AV. Cais de Apolo,435');
    cy.wait(100);
    cy.get(':nth-child(7) > .form-control').click().type('PE');
    cy.wait(100);
    cy.get('.col-md-8 > .form-control').click().type('teste2@gmail.com');
    cy.wait(100);
    cy.get(':nth-child(9) > .form-control').click().type('teste2@gmail.com');
    cy.wait(100);
    cy.get('.col-12 > .btn').click();
    cy.wait(1000);


    cy.get('[href="/cadastro_fornecedor/"] > .btn').click();
    cy.wait(1000);
    cy.get('.col-11 > .form-control').click().type('Xiaomi Inc');
    cy.wait(100);
    cy.get(':nth-child(3) > .form-control').click().type('12757700');
    cy.wait(100);
    cy.get(':nth-child(4) > .form-control').click().type('1387877');
    cy.wait(100);
    cy.get(':nth-child(5) > .form-control').click().type('121335');
    cy.wait(100);
    cy.get('.col-8 > .form-control').click().type('AV. Cais de Apolo, 666');
    cy.wait(100);
    cy.get(':nth-child(7) > .form-control').click().type('PE');
    cy.wait(100);
    cy.get('.col-md-8 > .form-control').click().type('teste2@gmail.com');
    cy.wait(100);
    cy.get(':nth-child(9) > .form-control').click().type('teste2@gmail.com');
    cy.wait(100);
    cy.get('.col-12 > .btn').click({force: true});
    cy.wait(1000);
    cy.get(':nth-child(2) > .nav-link').click();
    cy.wait(1000);
    cy.get('tbody > :nth-child(3) > :nth-child(1) > a > img').click();
    cy.wait(1000);
    cy.get(':nth-child(2) > .nav-link').click();
    cy.get('thead > tr > :nth-child(1)').should('not.contain', 'Xiaomi Inc');



  
  })
})
