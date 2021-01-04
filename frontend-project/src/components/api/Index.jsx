import React, {useState} from 'react';
import axios from 'axios';
import { TextField, Button } from "@material-ui/core";

function Address() {
    
    const [cep , setCep] = useState({cep: ''});
    const [info, setInfo] = useState({
        cep: '', 
        logradouro: '', 
        complemento: '', 
        bairro: '', 
        localidade: '',
        uf: '',
        ibge: '',
        gia: '',
    });

    
    const getInfo = () => {
        axios.get('http://viacep.com.br/ws/' + cep + '/json/')
            .then(response => {
                setInfo(response.data);
            });
    }

    const handlingCep = (e) => {
        setCep(e.target.value);
    }

    return(
        <>
            <h3>Consultando o CEP</h3>
            <TextField
                id="outlined-basic"
                label="CPF"
                variant="outlined"
                fullWidth='true'
                margin='normal'
                placeholder="Digite o CEP"
                onChange={(event) => {
                    handlingCep(event)
                }}/>
            
            <Button type='submit' onClick={ getInfo } variant='contained' color='primary'>
                Consultar
            </Button>

            <ul>
                <li>CEP:         { info['cep'] }</li>
                <li>Logradouro:  { info['logradouro'] }</li>
                <li>Complemento: { info['complemento'] }</li>
                <li>Bairro:      { info['bairro'] }</li>
                <li>Localidade:  { info['localidade'] }</li>
                <li>UF:          { info['uf'] }</li>
                <li>IBGE:        { info['ibge'] }</li>
                <li>GIA:         { info['gia'] }</li>
            </ul>
            
            
        </>
    )

}
 
export default Address;