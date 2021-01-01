import React, { useState, useEffect } from 'react';
import { Link ,useHistory} from 'react-router-dom';
import axios from 'axios';
import Loader from './Loader/Loader';
import { withRouter } from "react-router-dom";
//import './MovieSearch.css';
import {  Container, Col, Form,
  FormGroup, Label, Input,
  Button,Card, CardImg, CardImgOverlay, CardText, CardBody, CardTitle } from 'reactstrap';
import { Pagination, PaginationItem, PaginationLink } from 'reactstrap';


function MovieSearch(props) {


  const [data, setData] = useState([]);
  const [movieTitle, setMovieTitle] = useState('');
  const [pageNumbers, setPageNumbers] = useState([]);
  const [nameToSearch, setnameToSearch] = useState('');
  const [isLoading, setIsLoading] = useState(false);
 const [state , setState] = useState({
		  currentPage: 1,
		  pageNumber:1,
          dataPerPage: 10
     });



	const searchMovie = (e,number)=>{
	setIsLoading(true);

	axios.get('http://127.0.0.1:8000/search?q='+movieTitle+'&page='+number)
        .then(response => {
			console.log('response',JSON.stringify(response));
			setIsLoading(false);
			setData(response.data.Search);
			let pages = [];
			for (let i = 1; i <= Math.ceil(response.data.total / state.dataPerPage); i++) {
			pages.push(i);
			}
			setPageNumbers(pages);

	})

	}



  // Logic for displaying current data


   const handleClick = (e)=>{
		   e.preventDefault();
		   const {id , value} = e.target
         setState(prevState => ({
          ...prevState,
          currentPage : parseInt(e.target.id)
      }))
      }

   const handlePrev =()=>{
        if(state.currentPage === 1) return;

		let currentPageVal = parseInt(state.currentPage)-1;

         setState(prevState => ({
          ...prevState,
          currentPage : currentPageVal
      }))
    }
    const handleNext =()=>{
		let currentPageVal = parseInt(state.currentPage)+1;
        setState(prevState => ({
          ...prevState,
          currentPage : currentPageVal
      }))
    }




 return (

 <div className="container container-table">




    <div class="row mt-3 justify-content-center">
		<div class="col-md-8">
		 <h1 class="text-center">🦸 Superman IMDB</h1>
				<div class="input-group mb-3">
   <input
   className="form-control" placeholder="Search movie by title.." autocomplete="off" autofocus=""
     key="random1"
     value={movieTitle}
     placeholder={"search by movie title"}
     onChange={(e) => setMovieTitle(e.target.value)}
    />
    <div className="input-group-append">
      <button className="btn btn-outline-secondary" type="button" id="search-button" onClick={e=>searchMovie(e,1)} key="button" type="button">
       🔍
      </button>
    </div>
  </div>
    </div>
    </div>
 <div className="row vertical-center-row">

  {data && data.map((item,index) =>

  <div className="col-md-4">
    <Card key={index}>
        <CardImg top width="100%" src={item.poster_link} alt="Card image cap" />
        <CardBody>
          <CardTitle tag="h5">{item.title}</CardTitle>

        </CardBody>
      </Card>

	   </div>

  )}

  </div>



		<br/>
		<ul className="pagination pagination-sm">
  <li onClick={handlePrev} className="page-item"><a className="page-link" href="#">Previous</a></li>

  {data.length>0 && pageNumbers && pageNumbers.map((number,index) => (
  <li onClick={e=>searchMovie(e,number)} key={number} className="page-item"><a className="page-link" href="#">{number}</a></li>

  ))}

  <li  onClick={handleNext} className="page-item"><a className="page-link" href="#">Next</a></li>
</ul>


  </div>
)

}
export default withRouter(MovieSearch);
