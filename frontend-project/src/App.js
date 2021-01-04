import React from 'react'
import FormularioCadastro from './components/cadastro/FormularioCadastro';
import Address from './components/api/Index';
import {Container, Typography} from '@material-ui/core'
import './App.css';

function App() {
  return (
    <Container component='article' maxWidth='sm'>
      <Typography component='h1' variant='h3'>Formulário de Cadastro</Typography>
      <FormularioCadastro/>
      <Address/>
    </Container>


  );
}

export default App;
