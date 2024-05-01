describe('Valor_do_estoque', () => {

  it('O usuário excluiu um produto na lista de produtos cadastrados.', () => {
      cy.visit('https://stockgestordeploy.azurewebsites.net/');
      cy.get('.login-button').click();
      cy.wait(20); 
      cy.get('#username')
      
      
  })

  it('O usuário incluiu um produto na lista de produtos cadastrados.', () => {
      cy.visit('https://stockgestordeploy.azurewebsites.net/');
      cy.get('.login-button').click();
      cy.wait(20); 
      cy.get('#username')
      
     
  })
})