import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import './App.css';


import Records from './components/Records'
import Add  from './components/Add'
import Main from './components/Main'
import {Navbar} from './components/Navbar'

function App() {

  return (

    <Router>
      <Navbar />
      <Switch>
        <Route path='/records' component={Records}/>
        <Route path="/add" component={Add} />
        <Route path='/' component={Main}/>
      </Switch>
    </Router>

  );

}

export default App;
