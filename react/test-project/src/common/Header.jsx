import React from 'react'
import { Link } from 'react-router-dom'

function Header() {
  return (
    <>
    <div className='w-full h-20 flex flex-col justify-center items-center bg-blue-300'>
        <nav>
            <ul  className='flex gap-10'>
                <li className='cursor-pointer'> <Link to={'/'}>Home</Link></li>
                <li className='cursor-pointer'><Link to={'/about-us'}>About Us</Link></li>
                <li className='cursor-pointer'><Link to={'/contact'}>Contact</Link></li>
            </ul>
        </nav>
    </div>
    </>
  )
}

export default Header