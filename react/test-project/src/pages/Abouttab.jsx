import React from 'react';
import { useLocation } from 'react-router-dom';
import {data} from '../data/Aboutdata';
import Header from '../common/Header';

function Abouttab() {
    let useData=useLocation();
    let currId=(useData.pathname.split('/')[2])
    let currData=data.filter((v)=>v.id==currId)
  return (
    <div>
        <Header/>
        <div className='flex w-ful h-full justify-center items-center flex-col'>
            <p className='font-bolder text-2xl'>{currData[0].id}</p>
            <h1 className='font-bold '>{currData[0].title}</h1>
            <p>{currData[0].body}</p>
        </div>
    </div>
  )
}

export default Abouttab