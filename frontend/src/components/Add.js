import { Helmet } from 'react-helmet';
import { useState } from 'react'

const API = process.env.REACT_APP_API


function Add() {

    const [dato, setDato] = useState()

    const handleSubmit = async (e) => {
        e.preventDefault()
        const res = await fetch(`${API}/new`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                dato
            })
        })
        const data = await res.json()
        console.log(data)
        alert('ID inserted: '+data)
        setDato('')
    }


    return (

        <div className="App">
            <br />
            <Helmet>
                <title>Add data</title>
            </Helmet>
            <form onSubmit={handleSubmit}>
                <input className="newRecordText" type="text" placeholder='data' name="dato"
                    onChange = {e => setDato(e.target.value)}
                    value = {dato}
                    autoFocus
                /> <br />
                <input type="submit" value="Submit" className="newRecordSubmit" />
            </form>
        </div>

    );

}

export default Add;
