import { classNames } from 'shared/lib/classNames/classNames';
import { Page } from 'widgets/Page/Page';
import {
    ChangeEvent, FormEvent, memo, useCallback, useEffect, useState,
} from 'react';
import { MTable } from 'shared/UI/MTable';
import {
    DynamicModuleLoader,
    ReducersList,
}
    from 'shared/lib/DynamicModuleLoader/DynamicModuleLoader';
import { useAppDispatch } from 'shared/lib/hooks/useAppDispatch/useAppDispatch';
import { useSelector } from 'react-redux';
import { Loader } from 'shared/UI/Loader';
import {
    Alert, Button, Form, InputGroup, Modal,
} from 'react-bootstrap';
import { Theme, useTheme } from 'app/providers/ThemeProvider';
import { Card } from 'shared/UI/Card';
import { fetchCandidatesViaParameters } from 'pages/CandidatesPage/model/services/fetchCandidatesViaParameters';
import { CandidateTabs } from '../candidatesTabs/CandidatesTabs';
import { PageNavbar } from '../PageNavbar/PageNavbar';
import {
    CandidatesPageActions,
    CandidatesPageReducer,
    getComparedCandidates,
} from '../../model/slice/CandidatesPageSlice';
import {
    getCandidatesError,
    getCandidatesIds,
    getCandidatesIsLoading,
    getLowerAge,
    getLowerExp,
    getSearchString,
    getSelectedCandidates,
    getUpperAge,
    getUpperExp,
} from '../../model/selectors/candidatesPageSelectors';
import classes from './CandidatesPage.module.scss';
import { fetchCandidates } from '../../model/services/fetchCandidates';

interface CandidatesPageProps {
    className?: string;
}

const reducers: ReducersList = {
    candidates: CandidatesPageReducer,
};

const CandidatesPage = memo((props: CandidatesPageProps) => {
    const {
        className,
    } = props;

    const dispatch = useAppDispatch();
    const candidates = useSelector(getComparedCandidates.selectAll);
    const candidatesError = useSelector(getCandidatesError);
    const candidatesIsLoading = useSelector(getCandidatesIsLoading);
    const candidatesIds = useSelector(getCandidatesIds);
    const selectedCandidates = useSelector(getSelectedCandidates);
    const lowerAge = useSelector(getLowerAge);
    const upperAge = useSelector(getUpperAge);
    const lowerExp = useSelector(getLowerExp);
    const upperExp = useSelector(getUpperExp);
    const searchString = useSelector(getSearchString);

    const { theme } = useTheme();

    const [search, setSearch] = useState<string>('');
    const [isFocused, setIsFocused] = useState<boolean>(false);
    const [wasItFiltered, setWasItFiltered] = useState<boolean>(false);

    useEffect(() => {
        dispatch(fetchCandidates());

        // TODO: хоткиз для открытия окна поиска
        // const onKeypress = (e: any) => {
        //     const pressed = new Set();
        // };
        // document.addEventListener('keypress', onKeypress);
        //
        // return () => {
        //     document.removeEventListener('keypress', onKeypress);
        // };
    }, [dispatch]);

    const idsSetterHandler = useCallback((id: number) => {
        if (candidatesIds.includes(id)) {
            dispatch(CandidatesPageActions.setSelectedIds([
                ...candidatesIds
                    .filter((currentId) => currentId !== id),
            ]));

            dispatch(CandidatesPageActions.setSelectedCandidates([
                ...selectedCandidates
                    .filter((current) => current.id !== Number(id)),
            ]));
        } else {
            dispatch(CandidatesPageActions.setSelectedIds([
                ...candidatesIds,
                id,
            ]));

            dispatch(CandidatesPageActions.setSelectedCandidates([
                ...selectedCandidates,
                ...candidates
                    .filter((candidate) => candidate.id === Number(id)),
            ]));
        }
    }, [candidates, candidatesIds, dispatch, selectedCandidates]);

    // TODO: очистка списка выбранных кандидатов
    const clearCandidatesList = useCallback(() => {
        dispatch(CandidatesPageActions.setSelectedIds([]));
        dispatch(CandidatesPageActions.setSelectedCandidates([]));
    }, [dispatch]);

    const onSearchChangeHandler = useCallback((e: ChangeEvent<HTMLInputElement>) => {
        dispatch(CandidatesPageActions.setSearchString(e.target.value));
    }, [dispatch]);
    const onLowerAgeChangeHandler = useCallback((e: ChangeEvent<HTMLInputElement>) => {
        dispatch(CandidatesPageActions.setLowerAge(e.target.value as unknown as number));
    }, [dispatch]);
    const onUpperAgeChangeHandler = useCallback((e: ChangeEvent<HTMLInputElement>) => {
        dispatch(CandidatesPageActions.setUpperAge(e.target.value as unknown as number));
    }, [dispatch]);
    const onLowerExpChangeHandler = useCallback((e: ChangeEvent<HTMLInputElement>) => {
        dispatch(CandidatesPageActions.setLowerExp(e.target.value as unknown as number));
    }, [dispatch]);
    const onUpperExpChangeHandler = useCallback((e: ChangeEvent<HTMLInputElement>) => {
        dispatch(CandidatesPageActions.setUpperExp(e.target.value as unknown as number));
    }, [dispatch]);

    const onSearchCandidateSubmit = useCallback((e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        dispatch(fetchCandidatesViaParameters({
            education: searchString,
            lowerAge,
            upperAge,
            lowerExp,
            upperExp,
        }));

        setIsFocused(false);
        setWasItFiltered(true);
    }, [dispatch, lowerAge, lowerExp, searchString, upperAge, upperExp]);

    const resetFilters = useCallback(() => {
        dispatch(fetchCandidates());
        setWasItFiltered(false);
    }, [dispatch]);

    return (
        <DynamicModuleLoader reducers={reducers}>
            <Page className={classNames(classes.CandidatesPage, {}, [className])}>
                <Modal show={isFocused} onHide={() => setIsFocused(false)}>
                    <Card>
                        <h2>Поиск кандидатов</h2>
                        <Form
                            onSubmit={onSearchCandidateSubmit}
                        >
                            <InputGroup className="mb-3">
                                <Form.Control
                                    onChange={onSearchChangeHandler}
                                    value={searchString}
                                    placeholder="Поиск..."
                                />
                            </InputGroup>

                            <InputGroup className="mb-3">
                                <Form.Control
                                    placeholder="Возраст от"
                                    min={0}
                                    type="number"
                                    onChange={onLowerAgeChangeHandler}
                                    value={lowerAge}
                                />
                                <Form.Control
                                    placeholder="Возраст до"
                                    max={100}
                                    type="number"
                                    onChange={onUpperAgeChangeHandler}
                                    value={upperAge}
                                />
                            </InputGroup>
                            <InputGroup className="mb-3">
                                <Form.Control
                                    placeholder="Опыт работы от"
                                    min={0}
                                    type="number"
                                    onChange={onLowerExpChangeHandler}
                                    value={lowerExp}
                                />
                                <Form.Control
                                    placeholder="Опыт работы до"
                                    max={100}
                                    type="number"
                                    onChange={onUpperExpChangeHandler}
                                    value={upperExp}
                                />
                            </InputGroup>

                            <Button
                                type="submit"
                                variant="dark"
                            >
                                Поиск
                            </Button>
                        </Form>
                    </Card>
                </Modal>

                <PageNavbar
                    isCandidates={!!candidates?.length}
                    search={search}
                    setSearch={setSearch}
                    setIsFocused={setIsFocused}
                />
                {candidatesError && (
                    <Alert variant="danger">{`Упс... Произошла ошибка: ${candidatesError}`}</Alert>
                )}
                <div className={classes.content}>
                    <div className={classes.panelsWrapper}>
                        {candidatesIsLoading
                            ? <Card className={classes.loaderCard}><Loader /></Card>
                            : candidates.length
                                ? candidates.map((candidate) => (
                                    <CandidateTabs
                                        candidate={candidate}
                                        key={candidate.id}
                                        setSelectedId={idsSetterHandler}
                                    />
                                ))
                                : (
                                    <Card className={classes.loaderCard}>
                                        Никого не найдено
                                    </Card>
                                )}
                        {wasItFiltered && (
                            <Button
                                variant="danger"
                                onClick={resetFilters}
                            >
                                Сбросить фильтры
                            </Button>
                        )}
                    </div>

                    {selectedCandidates && (
                        <MTable
                            tableData={selectedCandidates}
                            clearCandidatesList={clearCandidatesList}
                        />
                    )}
                </div>
            </Page>
        </DynamicModuleLoader>

    );
});

export default CandidatesPage;
