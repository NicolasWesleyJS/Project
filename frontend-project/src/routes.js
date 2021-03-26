import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import FormularioCadastro from './alura/FormularioCadastro';

import SignIn from './pages/SignIn'

function Routes() {
    return(
        <BrowserRouter>
            <Switch>
                <Route path="/login" exact component={SignIn}/>
                <Route path="/cadastro" exact component={FormularioCadastro}/>

            </Switch> 
        </BrowserRouter>
    )
}

export default Routes;