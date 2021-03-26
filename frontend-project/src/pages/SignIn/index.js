import React, {useState} from 'react';
import { useHistory, useLocation} from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles'
import { Grid, Button, Avatar, TextField, Paper, Typography, Checkbox, FormControlLabel } from '@material-ui/core'
import CssBaseline from '@material-ui/core/CssBaseline';
// import api from '../../api'

import { create } from 'apisauce'

const api = create({
    baseURL: 'http://localhost:8000/api/v1/',
})

const useStyles = makeStyles((theme) => ({
    root: {
        height: '100vh',
    },
    paper: {
        margin: theme.spacing(8, 5),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }, 
      image: {
        backgroundImage: 'url(https://source.unsplash.com/random)',
        backgroundRepeat: 'no-repeat',
        backgroundColor:
          theme.palette.type === 'light' ? theme.palette.grey[50] : theme.palette.grey[900],
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      },
    form: {
        width: '90%', // Fix IE 11 issue.
        marginTop: theme.spacing(1),
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.primary.main,
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },

}));


function SignIn(props) {

    const classes = useStyles();

    const history = useHistory();

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const location = useLocation()




    const handleSubmit = async (e) => {
        e.preventDefault();
        if (email && password) {
            const response = await api.post('/token', {
                email: email,
                password: password
            })

            console.log(response)

            if (response.ok) {
                localStorage.setItem('token', response.data.access)
                localStorage.setItem('refresh', response.data.refresh)

                console.log(response)
    
                if (location.state && location.state.from) {
                    history.push(location.state.from)
    
                } else {
                    history.push('/home');
                }
            
            }
        }
    }


    
    return (
        <Grid container component='main' className={classes.root}> 
            <CssBaseline />
            <Grid item xs={false} sm={5} md={7} className={classes.image} />
            <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
                <div className={classes.paper}>
                    <Avatar className={classes.avatar} />
                    <Typography component="h1" variant="h5">
                        Sign in
                    </Typography>
                    <form className={classes.form}>
                        <TextField 
                            variant='outlined'
                            margin='normal'
                            required
                            fullWidth
                            id='email'
                            label='Email Address'
                            name='email'
                            autoComplete='email'
                            autoFocus
                            onChange={(e) => {setEmail(e.target.value)}}
                        />

                        <TextField 
                            variant='outlined'
                            margin='normal'
                            required
                            fullWidth
                            name='password'
                            label='Password'
                            type='password'
                            autoComplete='current-password'
                            onChange={(e) => {setPassword(e.target.value)}}
                        />

                        <FormControlLabel
                            control={<Checkbox value='Remember' color='primary' />}
                            label='Remember me'
                        />

                        <Button
                            type="submit"
                            fullWidth
                            variant="contained"
                            color="primary"
                            className={classes.submit}
                            // onSubmit={handleSubmit}
                        >
                            Sign In
                        </Button>

                    </form>
                </div>
            </Grid>

    
        </Grid>
    
    )    

}

export default SignIn;