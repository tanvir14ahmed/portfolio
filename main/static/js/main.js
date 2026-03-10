/* ============================================================
   TANVIR AHMED JOY — PORTFOLIO JAVASCRIPT
   Smooth scroll, typing animation, parallax, form handling
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

    // ========== NAVBAR ==========
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('nav-toggle');
    const navLinks = document.getElementById('nav-links');
    const navItems = document.querySelectorAll('.nav-link');

    // Scroll → sticky navbar background
    const handleNavScroll = () => {
        navbar.classList.toggle('scrolled', window.scrollY > 60);
    };
    window.addEventListener('scroll', handleNavScroll);

    // Mobile toggle
    navToggle?.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close mobile menu on link click
    navItems.forEach(link => {
        link.addEventListener('click', () => {
            navToggle?.classList.remove('active');
            navLinks?.classList.remove('active');
        });
    });

    // Highlight active nav on scroll
    const sections = document.querySelectorAll('section[id]');
    const highlightNav = () => {
        const scrollY = window.scrollY + 120;
        sections.forEach(section => {
            const top = section.offsetTop;
            const height = section.offsetHeight;
            const id = section.getAttribute('id');
            const link = document.querySelector(`.nav-link[href="#${id}"]`);
            if (link) {
                if (scrollY >= top && scrollY < top + height) {
                    navItems.forEach(item => item.classList.remove('active'));
                    link.classList.add('active');
                }
            }
        });
    };
    window.addEventListener('scroll', highlightNav);

    // ========== HERO PARTICLES ==========
    const particlesContainer = document.getElementById('particles');
    if (particlesContainer) {
        for (let i = 0; i < 40; i++) {
            const particle = document.createElement('div');
            particle.classList.add('particle');
            particle.style.left = `${Math.random() * 100}%`;
            particle.style.animationDelay = `${Math.random() * 8}s`;
            particle.style.animationDuration = `${6 + Math.random() * 6}s`;
            const size = 2 + Math.random() * 4;
            particle.style.width = `${size}px`;
            particle.style.height = `${size}px`;
            particle.style.opacity = `${0.1 + Math.random() * 0.5}`;
            particlesContainer.appendChild(particle);
        }
    }

    // ========== TYPING ANIMATION ==========
    const typingElement = document.getElementById('typing-text');
    if (typingElement) {
        const phrases = [
            'AI & Machine Learning Developer',
            'Django Full-Stack Specialist',
            'Python Enthusiast',
            'Problem Solver & Innovator',
            'Open Source Contributor'
        ];
        let phraseIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        const typeSpeed = 80;
        const deleteSpeed = 40;
        const pauseTime = 2000;

        function typeWriter() {
            const current = phrases[phraseIndex];

            if (!isDeleting) {
                typingElement.textContent = current.substring(0, charIndex + 1);
                charIndex++;
                if (charIndex === current.length) {
                    isDeleting = true;
                    setTimeout(typeWriter, pauseTime);
                    return;
                }
            } else {
                typingElement.textContent = current.substring(0, charIndex - 1);
                charIndex--;
                if (charIndex === 0) {
                    isDeleting = false;
                    phraseIndex = (phraseIndex + 1) % phrases.length;
                }
            }
            setTimeout(typeWriter, isDeleting ? deleteSpeed : typeSpeed);
        }
        setTimeout(typeWriter, 1500);
    }

    // ========== SCROLL REVEAL (IntersectionObserver) ==========
    const revealElements = document.querySelectorAll('.reveal');
    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    // Animate skill bars inside revealed element
                    const skillFills = entry.target.querySelectorAll('.skill-fill');
                    skillFills.forEach(fill => {
                        const width = fill.getAttribute('data-width');
                        if (width) {
                            setTimeout(() => {
                                fill.style.width = width + '%';
                            }, 300);
                        }
                    });
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -50px 0px'
        });

        revealElements.forEach(el => revealObserver.observe(el));
    }

    // Also animate any skill-fill that's not inside a .reveal
    const standaloneSkillFills = document.querySelectorAll('.skill-fill');
    if (standaloneSkillFills.length > 0) {
        const skillObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const width = entry.target.getAttribute('data-width');
                    if (width) {
                        setTimeout(() => {
                            entry.target.style.width = width + '%';
                        }, 300);
                    }
                }
            });
        }, { threshold: 0.5 });
        standaloneSkillFills.forEach(fill => skillObserver.observe(fill));
    }

    // ========== PROJECT MODAL ==========
    const modal = document.getElementById('project-modal');
    const modalClose = document.getElementById('modal-close');
    const modalTitle = document.getElementById('modal-title');
    const modalDescription = document.getElementById('modal-description');
    const modalTech = document.getElementById('modal-tech');
    const modalLinks = document.getElementById('modal-links');

    document.querySelectorAll('.project-modal-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const title = btn.dataset.title;
            const description = btn.dataset.description;
            const technologies = btn.dataset.technologies;
            const live = btn.dataset.live;
            const github = btn.dataset.github;

            if (modalTitle) modalTitle.textContent = title;
            if (modalDescription) modalDescription.textContent = description;

            if (modalTech) {
                modalTech.innerHTML = '';
                if (technologies) {
                    technologies.split(',').forEach(tech => {
                        const tag = document.createElement('span');
                        tag.classList.add('tech-tag');
                        tag.textContent = tech.trim();
                        modalTech.appendChild(tag);
                    });
                }
            }

            if (modalLinks) {
                modalLinks.innerHTML = '';
                if (live) {
                    const a = document.createElement('a');
                    a.href = live;
                    a.target = '_blank';
                    a.className = 'btn btn-primary';
                    a.innerHTML = '<i class="fas fa-external-link-alt"></i> Live Demo';
                    modalLinks.appendChild(a);
                }
                if (github) {
                    const a = document.createElement('a');
                    a.href = github;
                    a.target = '_blank';
                    a.className = 'btn btn-outline';
                    a.innerHTML = '<i class="fab fa-github"></i> GitHub';
                    modalLinks.appendChild(a);
                }
            }

            modal?.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    if (modalClose) {
        modalClose.addEventListener('click', closeModal);
    }
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal();
        });
    }
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });

    function closeModal() {
        modal?.classList.remove('active');
        document.body.style.overflow = '';
    }

    // ========== TESTIMONIALS SLIDER ==========
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    const dotsContainer = document.getElementById('testimonial-dots');
    let currentTestimonial = 0;
    let testimonialInterval;

    if (testimonialCards.length > 0 && dotsContainer) {
        // Create dots
        testimonialCards.forEach((_, index) => {
            const dot = document.createElement('button');
            dot.classList.add('testimonial-dot');
            if (index === 0) dot.classList.add('active');
            dot.setAttribute('aria-label', `Testimonial ${index + 1}`);
            dot.addEventListener('click', () => goToTestimonial(index));
            dotsContainer.appendChild(dot);
        });

        function goToTestimonial(index) {
            testimonialCards.forEach(card => card.classList.remove('active'));
            dotsContainer.querySelectorAll('.testimonial-dot').forEach(d => d.classList.remove('active'));
            testimonialCards[index].classList.add('active');
            dotsContainer.querySelectorAll('.testimonial-dot')[index].classList.add('active');
            currentTestimonial = index;
        }

        function nextTestimonial() {
            const next = (currentTestimonial + 1) % testimonialCards.length;
            goToTestimonial(next);
        }

        // Auto-play
        testimonialInterval = setInterval(nextTestimonial, 5000);

        // Pause on hover
        const slider = document.querySelector('.testimonials-slider');
        slider?.addEventListener('mouseenter', () => clearInterval(testimonialInterval));
        slider?.addEventListener('mouseleave', () => {
            testimonialInterval = setInterval(nextTestimonial, 5000);
        });
    }

    // ========== CONTACT FORM (AJAX) ==========
    const contactForm = document.getElementById('contact-form');
    const submitBtn = document.getElementById('contact-submit-btn');
    const formStatus = document.getElementById('form-status');

    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Reset errors
            document.querySelectorAll('.form-error').forEach(el => el.textContent = '');
            formStatus.className = 'form-status';
            formStatus.style.display = 'none';

            // Validate
            const name = contactForm.querySelector('[name="name"]').value.trim();
            const email = contactForm.querySelector('[name="email"]').value.trim();
            const message = contactForm.querySelector('[name="message"]').value.trim();
            let valid = true;

            if (!name) {
                document.getElementById('name-error').textContent = 'Please enter your name';
                valid = false;
            }
            if (!email || !isValidEmail(email)) {
                document.getElementById('email-error').textContent = 'Please enter a valid email';
                valid = false;
            }
            if (!message) {
                document.getElementById('message-error').textContent = 'Please enter a message';
                valid = false;
            }
            if (!valid) return;

            // Submit
            submitBtn.classList.add('loading');
            submitBtn.disabled = true;

            try {
                const response = await fetch(contactForm.action, {
                    method: 'POST',
                    body: new FormData(contactForm),
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                });

                const data = await response.json();

                if (data.success) {
                    formStatus.textContent = data.message;
                    formStatus.className = 'form-status success';
                    formStatus.style.display = 'block';
                    contactForm.reset();
                } else {
                    if (data.errors) {
                        Object.entries(data.errors).forEach(([field, error]) => {
                            const el = document.getElementById(`${field}-error`);
                            if (el) el.textContent = error;
                        });
                    }
                    formStatus.textContent = 'Please fix the errors above.';
                    formStatus.className = 'form-status error';
                    formStatus.style.display = 'block';
                }
            } catch (err) {
                formStatus.textContent = 'Something went wrong. Please try again.';
                formStatus.className = 'form-status error';
                formStatus.style.display = 'block';
            }

            submitBtn.classList.remove('loading');
            submitBtn.disabled = false;
        });
    }

    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    // ========== SMOOTH SCROLL for anchor links ==========
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

});
