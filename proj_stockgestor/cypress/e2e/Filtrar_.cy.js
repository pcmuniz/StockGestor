describe('Como usuário, eu gostaria de filtrar produtos por fornecedor', () => {
  it('Na lista de produtos devem aparecer apenas os produtos do fornecedor escolhido pelo usuário.(Apple)', () => {
    
    cy.visit('http://127.0.0.1:8000/');
    cy.get('.login-button').click();
    cy.wait(30); 
    cy.get('#username').type('cesarschool');
    cy.get('#password').type('Dj@ngo2024');
    cy.wait(1000);cy.get('.btn').click();
    cy.wait(100);

    cy.get('[href="/cadastro_produto/"] > .btn').click();
    cy.wait(100);
    cy.get(':nth-child(2) > .form-control').click().type('iPhone 15');
    cy.wait(100);
    cy.get(':nth-child(3) > .form-control').click().type('A15');
    cy.wait(100);
    cy.get(':nth-child(4) > .form-control').click().type('Apple Inc');
    cy.wait(100);
    cy.get(':nth-child(5) > .form-control').click().type('celular');
    cy.wait(100);
    cy.wait(100);
    cy.get(':nth-child(7) > .form-control').click().type('Apple Inc');
    cy.wait(100);
    cy.get('.col-md-8 > .form-control').click().type('2024-05-02');
    cy.wait(100);
    cy.get(':nth-child(9) > .form-control').click().type('2029-05-02');
    cy.wait(100);
    cy.get(':nth-child(10) > .form-control').click().type('2376493247');
    cy.wait(100);
    cy.get(':nth-child(11) > .form-control').click().type('2');
    cy.wait(100);
    cy.get(':nth-child(12) > .form-control').click().type('23243565');
    cy.wait(100);
    cy.get(':nth-child(13) > .form-control').click().type('2300');
    cy.wait(100);
    cy.get(':nth-child(14) > .form-control').click().type('512Gb Branco');
    cy.wait(100);
    cy.get('.d-flex > a > .btn').click();
    cy.wait(100);
    cy.get('.mt-2 > .btn').click();
    cy.wait(100);


    cy.get('[href="/cadastro_produto/"] > .btn').click();
    cy.wait(100);
    cy.get(':nth-child(2) > .form-control').click().type('iPhone 14 Pro');
    cy.wait(100);
    cy.get(':nth-child(3) > .form-control').click().type('A15');
    cy.wait(100);
    cy.get(':nth-child(4) > .form-control').click().type('Apple Inc');
    cy.wait(100);
    cy.get(':nth-child(5) > .form-control').click().type('celular');
    cy.wait(100);
    cy.get(':nth-child(7) > .form-control').click().type('Apple Inc');
    cy.wait(100);
    cy.get('.col-md-8 > .form-control').click().type('2024-05-02');
    cy.wait(100);
    cy.get(':nth-child(9) > .form-control').click().type('2029-05-02');
    cy.wait(100);
    cy.get(':nth-child(10) > .form-control').click().type('2376493247');
    cy.wait(100);
    cy.get(':nth-child(11) > .form-control').click().type('2');
    cy.wait(100);
    cy.get(':nth-child(12) > .form-control').click().type('23243565');
    cy.wait(100);
    cy.get(':nth-child(13) > .form-control').click().type('2600');
    cy.wait(100);
    cy.get(':nth-child(14) > .form-control').click().type('512Gb Branco');
    cy.wait(100);
    cy.get('.d-flex > a > .btn').click();
    cy.wait(100);
    cy.get('.mt-2 > .btn').click();
    cy.wait(100);


    cy.get('[href="/cadastro_produto/"] > .btn').click();
    cy.wait(100);
    cy.get(':nth-child(2) > .form-control').click().type('Galaxy S24');
    cy.wait(100);
    cy.get(':nth-child(3) > .form-control').click().type('S24');
    cy.wait(100);
    cy.get(':nth-child(4) > .form-control').click().type('Sansung Inc');
    cy.wait(100);
    cy.get(':nth-child(5) > .form-control').click().type('celular');
    cy.wait(100);
    cy.get(':nth-child(7) > .form-control').click().type('Samsung Inc');
    cy.wait(100);
    cy.get('.col-md-8 > .form-control').click().type('2024-05-02');
    cy.wait(100);
    cy.get(':nth-child(9) > .form-control').click().type('2029-05-02');
    cy.wait(100);
    cy.get(':nth-child(10) > .form-control').click().type('2376493247');
    cy.wait(100);
    cy.get(':nth-child(11) > .form-control').click().type('2');
    cy.wait(100);
    cy.get(':nth-child(12) > .form-control').click().type('23243565');
    cy.wait(100);
    cy.get(':nth-child(13) > .form-control').click().type('2300');
    cy.wait(100);
    cy.get(':nth-child(14) > .form-control').click().type('512Gb Branco');
    cy.wait(100);
    cy.get('.d-flex > a > .btn').click();
    cy.wait(100);
    cy.get('.mt-2 > .btn').click();
    cy.wait(100);



    cy.get('[href="/cadastro_produto/"] > .btn').click();
    cy.wait(100);
    cy.get(':nth-child(2) > .form-control').click().type('Xiaomi Readmi note 13');
    cy.wait(100);
    cy.get(':nth-child(3) > .form-control').click().type('X15');
    cy.wait(100);
    cy.get(':nth-child(4) > .form-control').click().type('Xiaomi Inc');
    cy.wait(100);
    cy.get(':nth-child(5) > .form-control').click().type('celular');
    cy.wait(100);
    cy.get(':nth-child(7) > .form-control').click().type('Xiaomi Inc');
    cy.wait(100);
    cy.get('.col-md-8 > .form-control').click().type('2024-05-02');
    cy.wait(100);
    cy.get(':nth-child(9) > .form-control').click().type('2029-05-02');
    cy.wait(100);
    cy.get(':nth-child(10) > .form-control').click().type('2376493247');
    cy.wait(100);
    cy.get(':nth-child(11) > .form-control').click().type('2');
    cy.wait(100);
    cy.get(':nth-child(12) > .form-control').click().type('23243565');
    cy.wait(100);
    cy.get(':nth-child(13) > .form-control').click().type('2300');
    cy.wait(100);
    cy.get(':nth-child(14) > .form-control').click().type('512Gb Branco');
    cy.wait(100);
    cy.get('.d-flex > a > .btn').click();
    cy.wait(100);
    cy.get('.mt-2 > .btn').click();
    cy.wait(100);

    cy.get('.form-select').select('Apple Inc.');
    cy.get('.row-cols-lg-auto > :nth-child(3) > .btn').click();

    cy.get('thead > tr > :nth-child(2)').should('not.contain', 'Xiaomi Inc', 'Samsung Inc');











    





  });


  
});
