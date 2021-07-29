import { useEffect, useState } from 'react'
import { Helmet } from 'react-helmet'

function Records() {
  const url = process.env.REACT_APP_API + '/all'
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
  // eslint-disable-next-line
  }, [temp]);

  const card = (dato, lastDato) => {
    return <section class="card">
      <p className="dato">Dato: {dato}</p>
      <p className="dato">Dato anterior: {lastDato}</p>
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
          return card(todo.block_data, todo.prev_hash)
        })
      }
    </div>
  );

}

export default Records;
