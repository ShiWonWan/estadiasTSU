import { Helmet } from 'react-helmet';
import '../App.css';

function Main() {

    return (

        <div className="App">
            <Helmet>
                <title>Main Page</title>
            </Helmet>
            <div className="portada">
                <h1 className="initialText">Blockchain<br />for data storage of computer equipment</h1>
            </div>
        </div>

    );

}

export default Main;
