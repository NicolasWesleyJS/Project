import React, {useState, useContext} from 'react';
import {Link, useHistory} from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles'
import { Grid, Button } from '@material-ui/core'


const useStyles = makeStyles((theme) => ({
    root: {
        height: '100vh',
    },

    paper: {
        margin: theme.spacing(8, 4),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center'
    },

    button: {
        background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
        border: 0,
        borderRadius: 3,
        boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
        color: 'white',
        height: 48,
        padding: '0 30px',
    }


}));


function SignIn(props) {

    const classes = useStyles();

    const history = useHistory();

    const [username, setUsername] = useState();
    const [password, setPassword] = useState();
    
    return (
        <Grid container component='main'> 


            <Grid item xs={12} sm={8} md={5} elevation={6} square className={classes.paper}>
                <Button className={classes.button}>Styled with Hook API</Button>
            </Grid>

    
        </Grid>
    
    )    

}

export default SignIn;