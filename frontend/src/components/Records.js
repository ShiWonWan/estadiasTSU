import { useEffect, useState } from 'react'
import { Helmet } from 'react-helmet'

function Records() {
  const url = 'http://localhost:5000/all'
  const [todos, setTodos] = useState()
  const [temp, setTemp] = useState(0)

  const fetchApi = async () => {
    const reponse = await fetch(url)
    const reponseJSON = await reponse.json()
    setTodos(reponseJSON)
  }



  useEffect(() => {
    setInterval(() => {
      setTemp((prevTemp) => prevTemp + 1)
    }, 2000)
  }, [])


  useEffect(() => {
    fetchApi()
  }, [temp]);

  const card = (date, dato, lastDato) => {
    return <section class="card">
      <p className="dato">Dato: {dato}</p>
      <p className="dato">Dato anterior: {lastDato}</p>
      <p className="date">Date: {date}</p>

    </section>
  }

  return (
    <div className="App">
      <br />
      <Helmet>
        <title>Records</title>
      </Helmet>
      <h1>Records</h1>
      {!todos ? 'Loading...' :
        todos.map((todo, index) => {
          return card(todo.date, todo.dato, todo['last dato'])
        })
      }
    </div>
  );

}

export default Records;
