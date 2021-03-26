import React, { useState } from "react";
import DadosPessoais from "./DadosPessoais";
import DadosUsuario from "./DadosUsuario";
import DadosEntrega from "./DadosEntrega";
import { Container } from "@material-ui/core"
function FormularioCadastro({ aoEnviar, validarCPF }) {
  return (
    <Container component='article' fullWidth='sm' >
        <DadosEntrega/>
    </Container>
  );
}

export default FormularioCadastro;
