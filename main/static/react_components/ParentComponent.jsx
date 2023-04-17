import React from 'react';

const ParentComponent = ({ objects }) => {
  return (
    <div className="row display-flex justify-content-start">
      {objects.map(object => (
        <div key={object.slug} className="col-lg-4 col-md-6 col-sm-12 mobiledevice">
          <article className="media content-section customhover" style={{ height: '95%' }}>
            <div className="media-body">
              <a href={`/${object.slug}`}>
                <img className="img-fluid" src="/" alt="" />
              </a>
              <div>
                <a className="article-title line-clamp-2 title-style" style={{ fontSize: '22px' }} href={`/${object.slug}`}>
                  {object.title}
                </a>
                <a href={`/${object.slug}`} style={{ textDecoration: 'none' }}>
                  <p className="article-content line-clamp-5 subtitle-style">{object.subtitle}</p>
                </a>
              </div>
            </div>
          </article>
        </div>
      ))}
    </div>
  );
};

export default ParentComponent;
