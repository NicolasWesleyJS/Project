import React, { useState } from 'react';
import { Button, TextField, Switch, FormControlLabel } from '@material-ui/core'

function FormularioCadastro() {

    const [login, setLogin] = useState("");
    const [senha, setSenha] = useState("");



    return (
        <form
            onSubmit={(event) => {
                event.preventDefault();
                console.log(login, senha);
            }}
        >
            <TextField
                id="outlined-basic"
                label="Login"
                variant="outlined"
                fullWidth='true'
                margin='normal'
                value = {login}
                onChange={(event) => {
                    login = setLogin(event.target.value)
                }}
            />

            <TextField
                value = {senha}
                id="outlined-basic"
                label="Senha"
                variant="outlined"
                fullWidth='true'
                margin='normal'
                onChange={(event) => {
                    senha = setSenha(event.target.value)
                }}
            />





            <Button type='submit' variant='contained' color='primary'>
                Cadastrar
            </Button>
        </form>
    );
}

export default FormularioCadastro;
