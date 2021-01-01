import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect
} from "react-router-dom";
import MovieSearch from './MovieSearch';


const Routes = (props)=>(

  <Router>
  <Switch>
  <Route exact path="/">
  <Redirect to="/search" />
  </Route> 
  <Route path="/search" component={MovieSearch} /> 
  </Switch>
  </Router>
 
)
export default Routes;
