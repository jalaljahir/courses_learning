import React from 'react';

const Socials: React.FC = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-4">Social Kit</h1>
      <p className="mb-8">Use these assets to share your experience at TechStack Conference!</p>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div>
          <h2 className="text-2xl font-bold mb-4">Logo</h2>
          <div className="bg-gray-200 p-8 rounded-lg">
            <img src="/logo.svg" alt="TechStack Conference Logo" className="w-full" />
          </div>
        </div>
        <div>
          <h2 className="text-2xl font-bold mb-4">Brand Details</h2>
          <div className="bg-gray-100 p-8 rounded-lg">
            <h3 className="text-xl font-bold">Social Tag</h3>
            <p className="mb-4">@techstackconf2026</p>

            <h3 className="text-xl font-bold">Official Hashtag</h3>
            <p className="mb-4">#TechStackConference</p>

            <h3 className="text-xl font-bold">Font</h3>
            <p className="mb-4 font-['Inter']">Inter</p>

            <h3 className="text-xl font-bold">Colors</h3>
            <div className="flex space-x-4">
              <div className="w-12 h-12 rounded-full" style={{ backgroundColor: '#fb7185' }}></div>
              <div className="w-12 h-12 rounded-full" style={{ backgroundColor: '#6366f1' }}></div>
              <div className="w-12 h-12 rounded-full" style={{ backgroundColor: '#0d2c2d' }}></div>
              <div className="w-12 h-12 rounded-full" style={{ backgroundColor: '#1d2f58' }}></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Socials;
