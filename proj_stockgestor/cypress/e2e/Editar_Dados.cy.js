describe('Editar Dados', () => {

  it('Como usuário, gostaria de editar dados cadastrados de um produto', () => {

      cy.visit('http://127.0.0.1:8000/');
      cy.wait(60);
      cy.get('.login-button').click();
      cy.wait(60); 
      cy.get('#username').type('cesarschool');
      cy.get('#password').type('Dj@ngo2024');
      cy.wait(60);
      cy.get('.btn').click();
      cy.wait(500);
      cy.get('[href="/cadastro_produto/"] > .btn').click();
      cy.wait(60);
      cy.get(':nth-child(2) > .form-control').type('AirJordam');
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
     cy.get(':nth-child(11) > .form-control').type('1');
     cy.wait(60);
     cy.get(':nth-child(12) > .form-control').type('2');
     cy.wait(60);
     cy.get(':nth-child(13) > .form-control').type('700');
     cy.wait(60);
     cy.get('.ms-auto > .form-control').type('Branco');
     cy.wait(2000);
     cy.get('.mt-2 > .btn').click();
     cy.wait(3000);
     cy.get('.table-danger > :nth-child(5) > .btn-success').click();
     cy.wait(60);
     cy.get(':nth-child(10) > .form-control').click().type('4');
     cy.wait(60);
     cy.get(':nth-child(12) > .form-control').click().type('900');
     cy.wait(60);
     cy.get('.ms-auto > .form-control').click().type('Branco');
     cy.wait(60);
     cy.get(':nth-child(7) > .form-control').type('2028-05-02');
     cy.wait(60);

cy.get('.table-default > :nth-child(3)').each(($el) => {
    const text = $el.text();
    const number = parseFloat(text);
    expect(number).to.be.greaterThan(2);
});

     

     
     
     














      

  })
})
