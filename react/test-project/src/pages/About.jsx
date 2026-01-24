import React from 'react';
import '../index.css';
import Header from '../common/Header';
import {data} from '../data/Aboutdata';
import { Link } from 'react-router-dom';

function About() {
  let allData=data.map((v,i)=>{
    return(
      <div className='border border-solid w-[250px] text-center' key={i}>
        <h1 className='font-bold'>{v.title}</h1>
        <p>{v.body}</p>
        <button className='border border-solid p-2 border-black bg-slate-200'><Link to={`/about-us/${v.id}`}>Read More</Link></button>  
      </div>
    )
  })
  return (
    <>
    <Header/>
    <div className='w-full'>
        <h1>About</h1>
        <div className='w-full flex flex-wrap gap-5'>
          {allData}
        </div>
    </div>
    </>
  )
}

export default About