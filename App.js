import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import CategoryList from './components/CategoryList';
import RecipeDetail from './components/RecipeDetail';

function App() {
    return (
        <Router>
            <Switch>
            <
            Route path="/" exact component={CategoryList} />
                            <Route path="/category/:id" component={RecipeList} />
                            <Route path="/recipe/:id" component={RecipeDetail} />
                        </Switch>
                    </Router>
                );
            }
export default App