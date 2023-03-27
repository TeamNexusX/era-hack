import { classNames } from 'shared/lib/classNames/classNames';
import { Page } from 'widgets/Page/Page';
import {
    ChangeEvent, memo, useCallback,
} from 'react';
import { useSelector } from 'react-redux';
import { getCandidatesIds, getSelectedCandidates } from 'pages/CandidatesPage';
import { MTable } from 'shared/UI/MTable';
import {
    Alert, Button, Form, OverlayTrigger, Tooltip,
} from 'react-bootstrap';
import { Theme, useTheme } from 'app/providers/ThemeProvider';
import { useNavigate } from 'react-router-dom';
import { useAppDispatch } from 'shared/lib/hooks/useAppDispatch/useAppDispatch';
import {
    DynamicModuleLoader,
    ReducersList,
} from 'shared/lib/DynamicModuleLoader/DynamicModuleLoader';
import {
    getComparisonError,
    getComparisonIsLoading,
    getComparisonPurpose,
} from '../../model/selectors/getComparisonData';
import classes from './ComparisonPage.module.scss';
import { CompareActions, CompareReducer } from '../../model/slice/CompareSlice';
import { compareCandidates } from '../../model/services/compareCandidates';

interface ComparisonPageProps {
    className?: string;
}

const reducers: ReducersList = {
    comparisonData: CompareReducer,
};

const ComparisonPage = memo((props: ComparisonPageProps) => {
    const {
        className,
    } = props;

    const { theme } = useTheme();
    const navigate = useNavigate();
    const dispatch = useAppDispatch();

    const selectedTask = useSelector(getComparisonPurpose);
    const selectedCandidates = useSelector(getSelectedCandidates);
    const selectedCandidatesIds = useSelector(getCandidatesIds);
    const compareError = useSelector(getComparisonError);
    const compareIsProcessing = useSelector(getComparisonIsLoading);

    const changeTaskHandler = useCallback((e: ChangeEvent<HTMLInputElement>) => {
        dispatch(CompareActions.setComparisonError(''));
        dispatch(CompareActions.setComparingPurpose(e.target.value));
    }, [dispatch]);

    const backendComparingHandler = useCallback(async () => {
        const result = await dispatch(compareCandidates({
            candidatesIds: selectedCandidatesIds,
            comparisonPurpose: selectedTask,
        }));

        if (result.meta.requestStatus === 'fulfilled') {
            navigate('/detailed_comparison');
        } else {
            console.log('Что-то пошло не так во время сравнения кандидатов');
        }
    }, [dispatch, navigate, selectedCandidatesIds, selectedTask]);

    if (!selectedCandidates.length) {
        return (
            <Page className={classNames(classes.ComparisonPage, {}, [className])}>
                <Alert
                    variant="warning"
                >
                    Похоже, Вы попали на эту страницу по ошибке.
                    Вернитесь на
                    {' '}
                    <Alert.Link href="/">главную</Alert.Link>
                    {' '}
                    или
                    {' '}
                    <Alert.Link href="/candidates">на страницу сравнения кандидатов</Alert.Link>
                </Alert>
            </Page>
        );
    }

    return (
        <DynamicModuleLoader reducers={reducers} removeAfterUnmount={false}>
            <Page className={classNames(classes.ComparisonPage, {}, [className])}>
                <h2 className={classes.header}>Выбранные кандидаты</h2>
                <MTable tableData={selectedCandidates} />

                <Form>
                    <Form.Control
                        onChange={changeTaskHandler}
                        value={selectedTask}
                        className={classes.select}
                        placeholder="Введите задачу, для которой надо найти кандидатов"
                    />

                    {compareError && (
                        <Alert variant="danger">
                            {compareError}
                        </Alert>
                    )}

                    {selectedTask.length < 10 || compareIsProcessing
                        ? (
                            <OverlayTrigger
                                placement="right"
                                delay={{ show: 100, hide: 500 }}
                                overlay={(
                                    <Tooltip>Введите не менее 10 символов</Tooltip>
                                )}
                            >
                                <span>
                                    <Button
                                        variant={theme === Theme.DARK ? 'info' : 'dark'}
                                        disabled={selectedTask.length < 10 || compareIsProcessing}
                                    >
                                        Перейти к углубленному сравнению
                                    </Button>
                                </span>
                            </OverlayTrigger>
                        )
                        : (
                            <Button
                                type="submit"
                                variant={theme === Theme.DARK ? 'info' : 'dark'}
                                disabled={selectedTask.length < 10 || compareIsProcessing}
                                onClick={backendComparingHandler}
                            >
                                Перейти к углубленному сравнению
                            </Button>
                        )}
                </Form>
            </Page>
        </DynamicModuleLoader>
    );
});

export default ComparisonPage;
