describe('Visualizar Detalhes', () => {

  it('Como usuário, gostaria de visualizar as informações cadastradas de um produto cadastrado', () => {

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
      cy.get(':nth-child(2) > .form-control').type('Creme de avelã Nutella 350g');
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
  
     cy.get(':nth-child(7) > .form-control').type('2028-05-02');
     cy.wait(60);

     cy.get('.form-select').select('NIKE BRASIL LTDA');
     cy.wait(60);  

     cy.get(':nth-child(9) > .form-control').type('200');
     cy.wait(60);
     cy.get(':nth-child(10) > .form-control').type('B6');
     cy.wait(60);
     cy.get(':nth-child(11) > .form-control').type('5');
     cy.wait(60);
     cy.get(':nth-child(12) > .form-control').type('2');
     cy.wait(60);
     cy.get(':nth-child(13) > .form-control').type('12.5');
     cy.wait(60);
     cy.get('.ms-auto > .form-control').type('Branco');
     cy.wait(60);
     cy.scrollTo('bottom');  
     cy.wait(60);
     cy.get('.d-flex > a > .btn').click({ force: true });
     cy.wait(2000);
     cy.get('.mt-2 > .btn').click();
     cy.wait(3000);
     cy.get(':nth-child(2) > :nth-child(5) > .btn-primary').click();
     cy.get('.show > .modal-dialog > .modal-content > .modal-body > .row > :nth-child(1) > .card > .card-body > :nth-child(2)').should('contain', 'Marca: Nutella');

  })
})
